import pickle

# Load FAISS metadata
with open("backend/faiss_index/index.pkl", "rb") as f:
    index_data = pickle.load(f)

# Check the tuple structure
print("Type of index.pkl content:", type(index_data))
print("Length of tuple:", len(index_data))

# # Print the first few elements
# for i, element in enumerate(index_data):
#     first_element = index_data[0]  # Access the first element correctly
#     print(f"First element: {first_element}\n")
#     print(f"Element {i}: Type -> {type(element)}")

#     if isinstance(element, dict):  # If it's a dictionary, print keys
#         print("Keys:", list(element.keys()))
#     elif isinstance(element, list):  # If it's a list, show the first few items
#         print("First few items:", element[:3])
#     else:  # For other types, print directly
#         print(element)

#     if i >= 2:  # Limit the number of elements printed
#         break
