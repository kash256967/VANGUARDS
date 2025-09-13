# profile.py

class Profile:
    def __init__(self, name, favorite_language, hobby, tech_stack, github_username, fun_fact):
        self.name = name
        self.favorite_language = favorite_language
        self.hobby = hobby
        self.tech_stack = tech_stack
        self.github_username = github_username
        self.fun_fact = fun_fact

    def introduce(self):
        print(f"Hi, I’m {self.name}. I love {self.favorite_language} and my hobby is {self.hobby}.")
        print(f"Fun fact about me: {self.fun_fact}\n")

    def show_stack(self):
        print("💻 My Tech Stack:")
        for tool in self.tech_stack:
            print(f" - {tool}")
        print()

    def github_link(self):
        return f"https://github.com/{self.github_username}"


# ---------- Example Usage ----------
if __name__ == "__main__":
    # Create your profile instance
    my_profile = Profile(
        name="JACOB KARUGABA",
        favorite_language="Python",
        hobby="painting",
        tech_stack=["Python", "Django", "Git", "Docker"],
        github_username="Jacob23-5522",
        fun_fact="I play both weiqi and chess!"
    )

    # Call methods
    my_profile.introduce()
    my_profile.show_stack()
    print("🔗 GitHub:", my_profile.github_link())