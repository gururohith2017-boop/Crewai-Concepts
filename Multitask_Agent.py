from crewai import Agent, Task, Crew, LLM
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()

# --------------------------------------------------
# 1. LLM
# --------------------------------------------------

llm = LLM(
    model="gpt-4o-mini",
    temperature=0.2
)

print("LLM created successfully!")

# --------------------------------------------------
# 2. AGENT
# --------------------------------------------------

marketing_agent = Agent(
    role="Signage Board Marketing Expert",

    goal=(
        "Help a signage and branding business approach potential clients, "
        "generate enquiries, convert enquiries into orders, and build "
        "long-term client relationships."
    ),

    backstory=(
        "You are an experienced marketing professional with extensive "
        "experience in signage boards, 3D letters, LED boards, entrance "
        "arches, promotional branding, vehicle advertising, fabrication "
        "and installation services. You understand how local businesses "
        "such as textile shops, jewellery stores, supermarkets, bakeries "
        "and other retail businesses make purchasing decisions."
    ),

    llm=llm,

    verbose=True
)

print("Marketing Agent created successfully!")

# --------------------------------------------------
# 3. TASK
# --------------------------------------------------

marketing_task = Task(

    description="""
You are advising a signage and branding business owner.

Create a practical client-approach strategy for getting signage
and branding orders from local businesses.

The business provides:

- Shop sign boards
- 3D letter boards
- LED letter boards
- Textile showroom signage
- Jewellery shop signage
- Supermarket signage
- Bakery signage
- Entrance arches
- Festival promotional branding
- Van and vehicle advertising
- Design, fabrication and installation

Explain how the business owner should approach potential clients
professionally and convert conversations into enquiries and orders.

Cover:

1. How to identify potential clients
2. How to make the first contact
3. How to introduce the business
4. What questions to ask the client
5. How to understand their signage requirement
6. How to present design ideas
7. How to discuss pricing professionally
8. How to follow up
9. How to handle "too expensive"
10. How to handle "we already have a vendor"
11. How to convert an enquiry into an order
12. How to maintain the client relationship
13. Common mistakes to avoid
14. Practical Do's and Don'ts
15. A short sample WhatsApp/call approach script
""",

    expected_output="""
Create the answer as a practical, easy-to-understand table.

Use these columns:

1. Step
2. What To Do
3. What To Say
4. Why It Works
5. Don't Do This

After the main table, provide:

A. 5 important Do's
B. 5 important Don'ts
C. A short WhatsApp approach script
D. A short phone-call script
E. A short follow-up script
F. 5 practical tips for converting enquiries into orders

Keep the advice practical for a local signage business.
Avoid generic marketing theory.
Focus on actions that can realistically help get signage,
arch, branding and vehicle-advertising orders.
""",

    agent=marketing_agent
)

print("Marketing Task created successfully!")

benefit_task = Task(
    description="""
    Take the result produced by the previous task.

    Based only on that result, write 5 simple sentences explaining
    the benefits of getting signage and branding work for the business.

    The sentences should be:
    - Simple and easy to understand
    - Practical
    - Focused on business benefits
    - Suitable for explaining to a signage business owner
    - Exactly 5 sentences
    """,
    expected_output="""
    Exactly 5 simple sentences describing the benefits of the
    signage and branding job.
    """,
    agent=marketing_agent,
    context=[marketing_task]
)
# --------------------------------------------------
# 4. CREW
# --------------------------------------------------

crew = Crew(
    agents=[marketing_agent],
    tasks=[marketing_task, benefit_task],
    verbose=True
)

print("Crew created successfully!")
# --------------------------------------------------
# 5. EXECUTE CREW
# --------------------------------------------------

result = crew.kickoff()

print("\n")
print("=" * 70)
print("FINAL MARKETING STRATEGY")
print("=" * 70)
print(result)