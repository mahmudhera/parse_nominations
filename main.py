import pandas as pd
from collections import Counter

if __name__ == '__main__':
    df = pd.read_csv('nominations.csv')
    post_names = list(df.columns)

    candidates_df = pd.read_csv('candidates', delimiter='\t', header=None)
    all_eligible_candidates = candidates_df[0].tolist()
    emails = candidates_df[1].tolist()

    for post_name in post_names:
        print('\n')
        print(post_name)
        nominated_candidates = df[post_name].tolist()
        dict = Counter(nominated_candidates)
        lst = []
        for nominated_candidate in dict.keys():
            if str(nominated_candidate) == 'nan':
                continue
            #print( f'{dict[nominated_candidate]}\t\t: {nominated_candidate}' )
            lst.append( (dict[nominated_candidate], nominated_candidate) )
        lst.sort(reverse=True)
        for pair in lst:
            print( f'{pair[1]} : {pair[0]}' )

'''
    for eligible_candidate, email in list(zip(all_eligible_candidates, emails)):
        nominated_posts = []
        for post_name in post_names:
            nominated_candidates = df[post_name].tolist()
            if eligible_candidate in nominated_candidates:
                nominated_posts.append(post_name)
        if len(nominated_posts) > 0:
            print(email)
            print(eligible_candidate)
            for post_name in nominated_posts:
                print(f'\t{post_name}')
'''
