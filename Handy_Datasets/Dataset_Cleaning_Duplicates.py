import pandas as pd
import os

def handle_duplicates(input_file, output_file=None):
    """
    Read a CSV file, identify duplicates, count them, show examples,
    and create a new file with duplicates removed.
    
    Args:
        input_file (str): Path to the input CSV file
        output_file (str, optional): Path to save the deduplicated CSV file.
                                    If None, will use input filename.
    """
    # Set default output filename if not provided
    if output_file is None:
        base_name = os.path.splitext(input_file)[0]
        output_file = f"{base_name}.csv"
    
    # Read the CSV file
    print(f"Reading CSV file: {input_file}")
    try:
        df = pd.read_csv(input_file)
    except Exception as e:
        print(f"Error reading file: {e}")
        return
    
    # Get the original row count
    total_rows = len(df)
    print(f"Total rows in the CSV: {total_rows}")
    
    # Identify and count duplicates
    duplicate_mask = df.duplicated(keep=False)
    duplicates = df[duplicate_mask]
    unique_duplicated_rows = duplicates.drop_duplicates()
    num_duplicate_sets = len(unique_duplicated_rows)
    num_duplicate_rows = len(duplicates) - num_duplicate_sets
    
    # Print duplicate statistics
    if num_duplicate_sets > 0:
        print(f"Found {num_duplicate_sets} sets of duplicated rows")
        print(f"Total number of extra/redundant rows: {num_duplicate_rows}")
        
        # Show examples of duplicates (up to 3 sets)
        print("\nExamples of duplicated rows:")
        for i, (_, group) in enumerate(df[duplicate_mask].groupby(list(df.columns))):
            if i >= 3:  # Limit to showing 3 examples
                break
            print(f"\nDuplicate set #{i+1} (appears {len(group)} times):")
            print(group.head(2).to_string(index=False))  # Show first 2 rows of each duplicate set
        
        # Remove duplicates, keeping the first occurrence
        df_deduped = df.drop_duplicates()
        deduped_rows = len(df_deduped)
        
        # Save the deduplicated data
        df_deduped.to_csv(output_file, index=False)
        print(f"\nDeduplication completed. Removed {total_rows - deduped_rows} duplicate rows.")
        print(f"Deduplicated CSV saved to: {output_file}")
    else:
        print("No duplicates found in the CSV file.")

if __name__ == "__main__":
    # Example usage
    input_file = input("Enter the path to your CSV file: ")
    handle_duplicates(input_file)