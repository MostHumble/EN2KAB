source_tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased", **special_tokens)
target_tokenizer = PreTrainedTokenizerFast.from_pretrained('Sifal/EN2KAB',token=key=user_secrets.get_secret("hftoken"))

def count_tokens(text, tokenizer):
    # Tokenize the text
    encoding = tokenizer.tokenize(text)
    # Return the number of tokens
    return len(encoding)

en_counts = list(df['en'].apply(lambda x: count_tokens(x, source_tokenizer)))
kab_counts = list(df['kab'].apply(lambda x: count_tokens(x, target_tokenizer)))

en_cumulative.sort()
kab_cumulative.sort()


def count_tokens(text, tokenizer):
    # Tokenize the text
    encoding = tokenizer.tokenize(text)
    # Return the number of tokens
    return len(encoding)

en_counts = list(df['en'].apply(lambda x: count_tokens(x, source_tokenizer)))
kab_counts = list(df['kab'].apply(lambda x: count_tokens(x, target_tokenizer)))

en_cumulative.sort()
kab_cumulative.sort()


# Calculate the cumulative distribution for filtered counts
en_cumulative = np.arange(1, len(en_filtered_counts) + 1) / len(en_filtered_counts)
kab_cumulative = np.arange(1, len(kab_filtered_counts) + 1) / len(kab_filtered_counts)

# Plot the cumulative distribution graph with more x ticks
plt.figure(figsize=(10, 6))
plt.plot(en_filtered_counts, en_cumulative, marker='.', linestyle='none', label='English', color='blue')
plt.plot(kab_filtered_counts, kab_cumulative, marker='.', linestyle='none', label='Kabyle', color='green')
plt.title('Cumulative Token Count Distribution (Filtered)')
plt.xlabel('Number of Tokens')
plt.ylabel('Cumulative Probability')
plt.legend()

# Customize the x-axis ticks
xticks = np.arange(0, max_threshold + 1, 1)  # Adjust the step value as needed
yticks = np.arange(0,1.1, 0.001)  # Adjust the step value as needed

plt.xticks(xticks, xticks)
plt.yticks(yticks, yticks)
plt.ylim(0.98, 1)
plt.xlim(18, max_threshold)

plt.grid(True)

plt.show()

# Calculate how many tokens we're leaving for en and kab
en_tokens_left = len(en_counts) - len(en_filtered_counts) * 0.996
kab_tokens_left = len(kab_counts) - len(kab_filtered_counts) * 0.997

# Print the number of tokens left for each language, rounded to 2 decimal places
print("Tokens left for English (en): {:.2f}".format(en_tokens_left))
print("Tokens left for Kabyle (kab): {:.2f}".format(kab_tokens_left))

# Calculate the number of sequences relative to the average number of tokens
en_sequences = en_tokens_left / np.mean(en_counts)
kab_sequences = kab_tokens_left / np.mean(kab_counts)

print("Number of sequences lost assuming an average sequence lenght of English (en): {:.2f}".format(en_sequences))
print("Number of sequences lost assuming an average sequence lenght of Kabyle (kab): {:.2f}".format(kab_sequences))