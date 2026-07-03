"""
DarijaBERT - Moroccan Darija BERT Model
Source: SI2M-Lab/DarijaBERT (Hugging Face)
"""

from transformers import AutoTokenizer, AutoModel, pipeline

print("🔍 Loading DarijaBERT model...")
print("Model: SI2M-Lab/DarijaBERT")
print("=" * 60)

# تحميل النموذج
tokenizer = AutoTokenizer.from_pretrained("SI2M-Lab/DarijaBERT")
model = AutoModel.from_pretrained("SI2M-Lab/DarijaBERT")

print("✅ Model loaded successfully!")
print(f"📊 Vocabulary size: {tokenizer.vocab_size}")
print(f"📊 Model parameters: {model.num_parameters():,}")

# اختبار Fill-Mask
print("\n" + "=" * 60)
print("🔍 Testing Fill-Mask capability...")
unmasker = pipeline('fill-mask', model='SI2M-Lab/DarijaBERT')

sentence = "اشنو [MASK] ليك"
results = unmasker(sentence)

print(f"\n📝 Sentence: {sentence}")
print("📊 Top predictions:")
for r in results[:3]:
    print(f"   - {r['sequence']} (score: {r['score']:.4f})")
