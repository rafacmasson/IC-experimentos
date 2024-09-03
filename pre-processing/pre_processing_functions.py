import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler


# Mapping the attacks into groups
def create_nslkdd_groups(df):
    # Define the rules to create the "group" column
    rules = {
        'dos': ['apache2', 'back', 'land', 'mailbomb', 'neptune', 'pod', 'processtable', 'smurf', 'teardrop', 'udpstorm'],
        'normal': ['normal'],
        'probe': ['mscan', 'satan', 'portsweep', 'ipsweep', 'nmap', 'saint'],
        'r2l': ['guess_passwd', 'warezmaster', 'snmpguess', 'snmpgetattack', 'httptunnel', 'multihop', 'named', 'sendmail', 'xlock', 'xsnoop', 'ftp_write', 'worm', 'phf', 'imap', 'spy', 'warezclient'],
        'u2r': ['buffer_overflow', 'ps', 'rootkit', 'xterm', 'loadmodule', 'perl', 'sqlattack']
    }

    # Maps the "attack" column to the "group" column using the rules
    df['group'] = df['label'].map({value: key for key, values in rules.items() for value in values})

    # Drops the "label" column
    df.drop(['label'], axis=1, inplace=True)

    # Returns the resulting DataFrame
    return df


# Standardization of attribute names
def standardize_names(df):
    df.columns = (
    df.columns.str.strip()
                .str.lower()
                .str.replace(' ', '_', regex=False)
                .str.replace('\(', '', regex=True)
                .str.replace('\)', '', regex=True)
    )

    return df


# Handling NaN and infinite values
def handle_nan_inf(df, attributes):
    for attribute in attributes:
        # Replace NaN values with 0
        df[attribute] = df[attribute].replace([np.nan, ",,"], 0)

        # Replace infinite values with -1
        df[attribute] = df[attribute].replace([np.inf, ",,"], -1)
        df.loc[df[attribute] == "Infinity", attribute] = -1

        # Convert values to numeric type
        df[attribute] = df[attribute].apply(pd.to_numeric)

    return df


# Handling non-numeric columns to numeric
def convert_to_numeric(df, attribute):
    # Incorrect typing when reading
    df[attribute] = pd.to_numeric(df[attribute], errors='coerce').fillna(0).astype(int)

    return df


# Handling categorical columns
def handle_categoricals(df, categorical_columns):
    # Save the last column of the original dataframe
    last_column = df.iloc[:, -1]

    # Remove the last column from the original dataframe
    df_no_last_column = df.drop(columns=df.columns[-1])

    # Apply one-hot encoding
    df_encoded = pd.get_dummies(df_no_last_column, columns=categorical_columns, dtype=int)

    # Concatenate the original last column back to the resulting dataframe
    result = pd.concat([df_encoded, last_column], axis=1)

    return result


# Handling attributes with many different categorical values
def handle_categorical_values(df, attributes):
    
    for attribute in attributes:
        # Identifying the top 5 categories for the attribute
        top_categories = df[attribute].value_counts().head(5).index.tolist()
        # Replacing categories not in the top 5 with 'others' for the attribute
        df.loc[~df[attribute].isin(top_categories), attribute] = 'others'

    return df


# Attribute removal
def remove_attributes(df, attributes):
    for attribute in attributes:
        df.drop([attribute], axis=1, inplace=True)

    return df


# Normalization
def normalize(train, test):
    # Separate features and labels
    X_train = train.iloc[:, :-1]  # Select all columns except the last
    y_train = train.iloc[:, -1]   # Select only the last column

    X_test = test.iloc[:, :-1]  # Select all columns except the last
    y_test = test.iloc[:, -1]   # Select only the last column

    # Initialize the MinMaxScaler object
    scaler = MinMaxScaler()

    # Fit the scaler only on the training data
    scaler.fit(X_train)

    # Apply normalization to training and test data
    X_train_scaled = scaler.transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Convert to DataFrame
    df_X_train = pd.DataFrame(X_train_scaled, columns=X_train.columns)
    df_X_test = pd.DataFrame(X_test_scaled, columns=X_test.columns)

    # Add the label column
    train_concat = pd.concat([df_X_train, y_train], axis=1)
    test_concat = pd.concat([df_X_test, y_test], axis=1)

    return train_concat, test_concat