import pandas as pd


class User:
    def __init__(self, name):
        df = pd.read_csv('../data/users.csv')
        self.name = name
        if name not in df['username'].unique():
            self.foodHistory = {"protein_val": 0,
                                "fat_val": 0,
                                "carbs_val": 0,
                                "calories_val": 0,
                                "sugar_val": 0,
                                "caffeine_val": 0,
                                "fibre_val": 0,
                                "calcium_val": 0,
                                "iron_val": 0,
                                "sodium_val": 0,
                                "cholesterol_val": 0}
            self.update_to_csv(self.foodHistory['protein_val'],
                               self.foodHistory['fat_val'],
                               self.foodHistory['carbs_val'],
                               self.foodHistory['calories_val'],
                               self.foodHistory['sugar_val'],
                               self.foodHistory['caffeine_val'],
                               self.foodHistory['fibre_val'],
                               self.foodHistory['calcium_val'],
                               self.foodHistory['iron_val'],
                               self.foodHistory['sodium_val'],
                               self.foodHistory['cholesterol_val'])
        else:
            row = df[df['username'] == name]
            self.foodHistory = {"protein_val": row['protein_val'],
                                "fat_val": row['fat_val'],
                                "carbs_val": row['carbs_val'],
                                "calories_val": row['calories_val'],
                                "sugar_val": row['sugar_val'],
                                "caffeine_val": row['caffeine_val'],
                                "fibre_val": row['fibre_val'],
                                "calcium_val": row['calcium_val'],
                                "iron_val": row['iron_val'],
                                "sodium_val": row['sodium_val'],
                                "cholesterol_val": row['cholesterol_val']
                                }

    def update_to_csv(self, protein, fats, carbs, calories, sugar, caffeine, fibre, calcium, iron, sodium, cholesterol):
        # df = pd.read_csv("../data/users.csv", index=False)
        df_user = pd.DataFrame({"username": self.name,
                                "protein_val": protein,
                                "fat_val": fats,
                                "carbs_val": carbs,
                                "calories_val": calories,
                                "sugar_val": sugar,
                                "caffeine_val": caffeine,
                                "fibre_val": fibre,
                                "calcium_val": calcium,
                                "iron_val": iron,
                                "sodium_val": sodium,
                                "cholesterol_val": cholesterol
                                }, index=[0])
        # df_user = df_user.reset_index(drop=True)
        # df = pd.concat([df, df_user], ignore_index=True, axis=0)
        # df = df.reset_index(drop=True)
        df_user.to_csv('../data/users.csv', mode = 'a', index=False, header = False)

    def __str__(self):
        return (self.name, self.foodHistory)
