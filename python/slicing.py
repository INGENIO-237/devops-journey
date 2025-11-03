planet1 = "Closest of sun"
planet2 = "Second from sun"

print(planet1[0:7])  # Closest
print(planet2[0:7])  # Second

# Syntax: string[start:end:step]
# start: starting index (inclusive)
# end: ending index (exclusive)
# step: step size (optional)

print(planet1[0:7:2])  # Clos
print(planet1[8:])  # of sun
print(planet1[::2])

devops = (
    "Linux",
    "Docker",
    "Kubernetes",
    "Terraform",
    "Jenkins",
    "Git",
    "AWS",
    "Python",
    "Ansible",
)

print(devops[0:4])  # ('Linux', 'Docker', 'Kubernetes', 'Terraform')
print(devops[4:])  # ('Jenkins', 'Git', 'AWS', 'Python', 'Ansible')

skills = {
    "devops": (
        "Linux",
        "Docker",
        "Kubernetes",
        "Terraform",
        "Jenkins",
        "Git",
        "AWS",
        "Python",
        "Ansible",
    ),
    "dev": [
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "Node.js",
        "Angular",
        "Vue.js",
        "Django",
        "Flask",
    ],
}

print(skills["devops"][2:5])  # ('Kubernetes', 'Terraform', 'Jenkins')
print(skills["dev"][0:3])  # ['HTML', 'CSS', 'JavaScript']
