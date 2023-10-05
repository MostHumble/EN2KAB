from tokenizers.processors import TemplateProcessing


def addPreprocessing(tokenizer):
  """Adds the capability to wrap a sentence between bos and aos tokens"""
  tokenizer._tokenizer.post_processor = TemplateProcessing(
      single=tokenizer.bos_token + " $A " + tokenizer.eos_token,
      special_tokens=[(tokenizer.eos_token, tokenizer.eos_token_id), (tokenizer.bos_token, tokenizer.bos_token_id)])