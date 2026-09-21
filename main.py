import os
from openai import OpenAI

# Initialize client with secure environment variable parsing
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def generate_support_reply(customer_email_text, company_kb):
    """
    Ingests unstructured customer inquiries, runs context processing against 
    a localized corporate knowledge base, and returns a high-retention draft.
    """
    system_prompt = (
        "You are an enterprise customer success operations bot. "
        f"Draft a concise, professional reply using only this knowledge base: {company_kb}"
    )
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": customer_email_text}
            ],
            temperature=0.3  # Low temperature ensures deterministic, non-hallucinated results
        )
        return response.choices.message.content
    except Exception as e:
        return f"Operational Error during text generation pipeline: {str(e)}"

# Test execution simulate a common corporate software bottleneck
knowledge_base = "Enterprise subscription pricing is $49/month. Standard refund policy window is 14 days post-purchase."
incoming_query = "Hi, I bought the operational tooling package 3 days ago but it doesn't fit my workflow. Am I eligible for a return?"

if __name__ == "__main__":
    print("--- Initializing AI Customer Automation Thread ---")
    draft_reply = generate_support_reply(incoming_query, knowledge_base)
    print(draft_reply)
