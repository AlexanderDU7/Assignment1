import pandas as pd

def clean(input_file1, input_file2):
    data1 = pd.read_csv(input_file1)
    data2 = pd.read_csv(input_file2)
    # merge the two input data files based on the ID of each respondent.
    df = pd.merge(data1, data2, left_on='respondent_id', right_on='id').drop('id', axis=1)
    # drop any rows with missing values.
    clean_na = df.dropna()
    # drop rows if the job value contains ‘insurance’ or ‘Insurance’.
    cleaned = clean_na[clean_na['job'].str.contains('Insurance|insurance') == False]
    return cleaned

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('contact_info_file', help='The path to the respondent_contact.csv file')
    parser.add_argument('other_info_file', help='The path to the respondent_other.csv file')
    parser.add_argument('output_file', help='The path to the output file')
    args = parser.parse_args()

    cleaned_file = clean(args.contact_info_file, args.other_info_file)
    cleaned_file.to_csv(args.output_file, index=False)
