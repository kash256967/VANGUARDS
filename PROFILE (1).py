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
        print(f"Fun fact about me: {self.fun_fact}")

    def show_stack(self):
        print(f"{self.name}'s Tech Stack:")
        for i, tool in enumerate(self.tech_stack, start=1):
            print(f"  {i}. {tool}")

    def github_link(self):
        return f"https://github.com/{self.github_username}"


# Example usage
if __name__ == "__main__":
    my_profile = Profile(
        name="SERAH KENKYERENGYE",
        favorite_language="Python",
        hobby="painting",
        tech_stack=[ "Git","Python", "SQL"],
        github_username="Serahm47",
        fun_fact="I once coded for 6 hours straight!"
    )

    my_profile.introduce()
    my_profile.show_stack()
    print("GitHub Profile:", my_profile.github_link())
