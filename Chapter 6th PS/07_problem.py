post = "Perry is a brilliant programmer.\nHe everyday tries to learn something new.\nHe is currently learning python."


if (
    "Perry".lower() in post.lower() #converting both perry to lower case and the entire post also
):  # Lower is used if Perry is written as perry it will still detect as it will convert Perry to all lower and detect with the lowner case powt.

    print("This post is about Perry")
else:
    ("This post is not about Perry")
# End of program
