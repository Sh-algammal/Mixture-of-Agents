import streamlit as st
import asyncio
import os
from openai import AsyncOpenAI

# Set up the Streamlit app
st.title("Mixture-of-Agents")

# Get API key
hf_api_key = st.text_input("Enter your Hugging Face Access Token:", type="password")

# Define models (Using the router requires exact model IDs)
reference_models = [
    "Qwen/Qwen2.5-7B-Instruct", 
    "deepseek-ai/DeepSeek-V3.2-Exp",
    "meta-llama/Llama-3.1-8B-Instruct"
]

aggregator_model = "meta-llama/Llama-3.1-8B-Instruct"

if hf_api_key:
    client = AsyncOpenAI(
        base_url="https://router.huggingface.co/v1",
        api_key=hf_api_key,
    )

    user_prompt = st.text_input("Enter your question:")

    async def run_llm(model):
        """Run a single LLM call using the new Router URL."""
        try:
            response = await client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": user_prompt}],
                temperature=0.7,
                max_tokens=512,
            )
            return model, response.choices[0].message.content
        except Exception as e:
            return model, f"Error: {str(e)}"

    async def main():
        with st.spinner('Asking agents via new Router...'):
            results = await asyncio.gather(*[run_llm(model) for model in reference_models])
        
        # Display individual model responses
        st.subheader("Individual Model Responses:")
        valid_responses = []
        
        for model, response in results:
            with st.expander(f"Response from {model[:model.find('/')].title()}"):
                st.write(response)
                if not response.startswith("Error"):
                    valid_responses.append(response)
        
        # Aggregate responses
        st.subheader("Aggregated Response:")
        
        if not valid_responses:
            st.error("All models failed. Check Internet or Token permissions.")
            return

        aggregator_system_prompt = "You are a smart synthesizer. Summarize and combine the following responses into one perfect answer:\n\n"
        combined_content = aggregator_system_prompt + "\n---\n".join(valid_responses)

        try:
            stream = await client.chat.completions.create(
                model=aggregator_model,
                messages=[{"role": "user", "content": combined_content}],
                max_tokens=1024,
                stream=True,
            )
            
            response_container = st.empty()
            full_response = ""
            
            async for chunk in stream:
                if chunk.choices and len(chunk.choices) > 0:
                    content = chunk.choices[0].delta.content or ""
                    full_response += content
                    response_container.markdown(full_response + "▌")
            response_container.markdown(full_response)
            
        except Exception as e:
            st.error(f"Aggregation Error: {str(e)}")

    if st.button("Get Answer"):
        if user_prompt:
            asyncio.run(main())
        else:
            st.warning("Please enter a question.")

else:
    st.warning("Please enter your Hugging Face Access Token.")