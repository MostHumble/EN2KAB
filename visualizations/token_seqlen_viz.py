def count_tokens(text, tokenizer):
    # Tokenize the text
    encoding = tokenizer.tokenize(text)
    # Return the number of tokens
    return len(encoding)

en_counts = list(df['en'].apply(lambda x: count_tokens(x, source_tokenizer)))
kab_counts = list(df['kab'].apply(lambda x: count_tokens(x, target_tokenizer)))
en_counts.sort()
kab_counts.sort()

# Plot the filtered token count distributions
def token_count_distributions(kab_counts, en_counts, bins=100, xlim=50):
    plt.figure(figsize=(10, 6))
    
    plt.subplot(1, 2, 1)
    plt.hist(en_counts, bins=bins, color='blue', alpha=0.7)
    plt.title('English Token Count Distribution')
    plt.xlabel('Number of Tokens')
    plt.ylabel('Frequency')
    plt.xlim(0, 50)
    
    plt.subplot(1, 2, 2)
    plt.hist(kab_counts, bins=bins, color='green', alpha=0.7)
    
    plt.xlim(0, xlim)
    
    plt.title('Kabyle Token Count Distribution ')
    plt.xlabel('Number of Tokens')
    plt.ylabel('Frequency')
    
    plt.tight_layout()
    plt.show()

def  cumulative_distribution(kab_counts, en_counts, max_threshold=25):
    
    # Calculate the cumulative distribution for filtered counts
    en_cumulative = np.arange(1, len(en_counts) + 1) / len(en_counts)
    kab_cumulative = np.arange(1, len(kab_counts) + 1) / len(kab_counts)
    
    # Plot the cumulative distribution graph with more x ticks
    plt.figure(figsize=(10, 6))
    plt.plot(en_counts, en_cumulative, marker='.', linestyle='none', label='English', color='blue')
    plt.plot(kab_counts, kab_cumulative, marker='.', linestyle='none', label='Kabyle', color='green')
    plt.title('Cumulative Token Count Distribution ')
    plt.xlabel('Number of Tokens')
    plt.ylabel('Cumulative Probability')
    plt.legend()
    
    # Customize the x-axis ticks
    xticks = np.arange(0, max_threshold + 1, 1)  # Adjust the step value as needed
    #yticks = np.arange(0,1.1, 0.001)  # Adjust the step value as needed
    
    plt.xticks(xticks, xticks)
    #plt.yticks(yticks, yticks)
    plt.ylim(0.98, 1)
    plt.xlim(15, max_threshold)
    
    plt.grid(True)
    plt.show()

def show_lost(kab_counts ,en_counts, kab_tresh = 22, en_tresh = 21):
    en_filtered_counts = [x for x in en_counts if x <= en_tresh]
    kab_filtered_counts = [x for x in kab_counts if x <= kab_tresh]
    
    # Calculate how many tokens we're leaving for en and kab
    en_tokens_left = len(en_counts) - len(en_filtered_counts) 
    kab_tokens_left = len(kab_counts) - len(kab_filtered_counts)
    
    # Print the number of tokens left for each language, rounded to 2 decimal places
    print("Tokens left for English (en): {:.2f}".format(en_tokens_left))
    print("Tokens left for Kabyle (kab): {:.2f}".format(kab_tokens_left))
    
    # Calculate the number of sequences relative to the average number of tokens
    en_sequences = en_tokens_left / np.mean(en_counts)
    kab_sequences = kab_tokens_left / np.mean(kab_counts)
    
    print("Number of sequences lost assuming an average sequence lenght of English (en): {:.2f}".format(en_sequences))
    print("Number of sequences lost assuming an average sequence lenght of Kabyle (kab): {:.2f}".format(kab_sequences))
