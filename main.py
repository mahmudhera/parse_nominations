import pandas as pd
from collections import Counter

if __name__ == '__main__':
    df = pd.read_csv('nominations.csv')
    post_names = list(df.columns)

    f = open('candidates', 'r')
    lines = f.readlines()
    all_eligible_candidates = [ line.strip() for line in lines ]
    f.close()

    for post_name in post_names:
        print(post_name)
        nominated_candidates = df[post_name].tolist()
        dict = Counter(nominated_candidates)
        for nominated_candidate in dict.keys():
            if str(nominated_candidate) == 'nan':
                continue
            print( f'{dict[nominated_candidate]}\t\t: {nominated_candidate}' )


    for eligible_candidate in all_eligible_candidates:
        nominated_posts = []
        for post_name in post_names:
            nominated_candidates = df[post_name].tolist()
            if eligible_candidate in nominated_candidates:
                nominated_posts.append(post_name)
        if len(nominated_posts) > 0:
            print(eligible_candidate)
            for post_name in nominated_posts:
                print(f'\t{post_name}')
