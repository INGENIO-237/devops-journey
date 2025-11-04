"""
Here we test our knowledge on datatypes and conditions
"""

devops = [
    "Jenkins",
    "Docker",
    "Kubernetes",
    "Terraform",
    "Ansible",
    "Git",
    "Python",
    "Linux",
    "AWS",
    "GCP",
    "Azure",
    "Jira",
    "Kali Linux",
]

dev = (
    "NodeJS",
    "React",
    "Angular",
    "VueJS",
    "Django",
    "Flask",
    "Ruby on Rails",
    "Spring Boot",
)

user_skill = input("Enter your skill: ")

if user_skill in devops:
    print(f"You have DevOps skill: {user_skill}")
elif user_skill in dev:
    print(f"You have Development skill: {user_skill}")
else:
    print(f"Skill {user_skill} is not in our list")
