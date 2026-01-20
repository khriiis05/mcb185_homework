gunzip -c ../MCB185/data/dictionary.gz | grep -E "[r]" | grep -E "^[oznrica]{4,}$"
gunzip -c ../MCB185/data/dictionary.gz | grep -E "[r]" | grep -E "^[oznrica]{4,}$" | wc -l
