
# MUST CHANGE FOR EACH USECASE
path = "/Users/roccojemilo/Desktop/Python Scripts/Banquet/outputs/create_question_skeleton.txt"

with open(path, "w") as file:
    for i in range(1, 35):
        file.write(f"""
                    #q{i}
                    q{i}_df = pd.read_sql(\"""
                        SELECT *
                        FROM
                    \""", conn)
                    display(q{i}_df)
                    q{i}_df.to_pickle("q{i}.pkl")
                    """)

print("Successfully question skeleton")
