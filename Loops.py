# name = "Shubham" 
# for i in name:
#     print(i)
# # for i in range(90):
# #     print(i)
# #range is funation in which we range( kitne baar run karna hai vo likhna hai )
# for i in range(0,20,5):
#     print(int(i))

import hashlib

def calculate_love_percentage(name1: str, name2: str) -> int:
    """
    Computes a deterministic compatibility percentage (0-100%)
    using SHA-256 hashing on normalized name pairs.
    """
    # 1. Normalize and sort to ensure commutative property (A + B == B + A)
    n1 = name1.strip().lower()
    n2 = name2.strip().lower()
    combined_pair = "".join(sorted([n1, n2]))
    
    # 2. Generate a deterministic SHA-256 digest
    hash_digest = hashlib.sha256(combined_pair.encode()).hexdigest()
    
    # 3. Map hex to an integer range between 40% and 99%
    seed_val = int(hash_digest[:8], 16)
    percentage = 40 + (seed_val % 60)
    return percentage

def calculate_flames(name1: str, name2: str) -> str:
    """
    Classic FLAMES algorithm:
    F = Friends, L = Love, A = Affection, M = Marriage, E = Enemy, S = Siblings
    """
    s1 = list(name1.strip().lower().replace(" ", ""))
    s2 = list(name2.strip().lower().replace(" ", ""))
    
    # Remove common characters
    for char in s1[:]:
        if char in s2:
            s1.remove(char)
            s2.remove(char)
            
    count = len(s1) + len(s2)
    if count == 0:
        return "Same person / Identical names"
    
    flames = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]
    
    idx = 0
    while len(flames) > 1:
        idx = (idx + count - 1) % len(flames)
        flames.pop(idx)
        
    return flames[0]

# --- Demo Execution ---
if __name__ == "__main__":
    p1 = "Shubham"
    p2 = ""
    
    score = calculate_love_percentage(p1, p2)
    relation = calculate_flames(p1, p2)
    
    print(f"Results for {p1} & {p2}:")
    print(f"• Compatibility Score: {score}%")
    print(f"• FLAMES Verdict: {relation}")