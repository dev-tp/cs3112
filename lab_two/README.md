# Assignment Two

## 1. Implement Selection Sort

Consider sorting n numbers of elements inside array A by first finding the smallest element of A and exchangng it with A[1], then find the second smallest element of A, and exchange it with A[2]. Continue in this manner for the first n - 1 elements of A.

## 2. Implement Insertion Sort

## 3. Transform a free tree into a rooted tree
The free tree and the root are input by the user, and for the rooted tree, you output it level by level. **Hint:** Use Adjacency Matrix or Adjacency Lists to store the tree, and implement the transformation using queue.

**Example input for question three:**

    i _ d _
    c b a e
    h g _ f

    transform_free_tree_to_rooted_tree(["i_d_", "cbae", "hg_f"])

**Example output for question three:**

    a
    b d e
    c g f
    h i