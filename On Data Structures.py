"""
On data structures and comparisons based on a set of fundamental algorithms

################
# Content List #
################

1. List of data structures
    1.1 Arrays
        1.1.1 Background information
        1.1.2 Basic Operations
        1.1.3 Sorting Algorithms
    1.2 Heaps
        1.2.1 Background information
        1.2.2 Basic Operations
            1.2.2.1 max_heapify()
            1.2.2.2 build_maxheap()
            1.2.2.3 Min-heap variations
        1.2.3 Sorting Algorithms
    1.3 Binary Search Trees (BST)
        1.3.1 Background information
        1.3.2 Basic Operations
        1.3.3 Traversal
        1.3.4 Sort for BST
        1.3.5 Rotations
        1.3.6 AVL Trees
            1.3.6.1 Data Structure Augmentation
            1.3.6.2 Background Information
            1.3.6.3 Code Reference
            1.3.6.4 Self-balancing function
            1.3.6.5 Complexity and Efficiency
    1.4 Linked list (upcoming)
    1.5 Stacks (upcoming)
    1.6 Queues (upcoming)

##############################
# 1. List of data structures #
##############################

1.1 Arrays

    1.1.1 Background information

    Arrays are defined as the following (wikipedia): A data structure consisting
    of a collection of elements (values or variables), each identified by at
    least one array index or key. Examples of arrays in python include lists,
    strings.

    Arrays have a long history, attributed to the fact that most computers, storage
    devices utilise a one-dimensional array of words as the basis for the memory.
    Consequently, to effectively exploit the addressing logic of computers,
    addresses are often used as indexes.

    Dictionaries in python are not considered to be arrays due to the requirement
    that elements in arrays have the same size and should use the same data
    representation. This feature allows a single iterative statement to process
    through every element of the array.
    
    1.1.2 Basic Operations

        --------------------------
        | Operation | Complexity |
        --------------------------
        |   get(i)  |    O(1)    |
        |   set(i)  |    O(1)    |
        --------------------------
        Table 1. Access complexities for arrays 

        The above is a table of complexities for basic operations that forms the
        basis to more complex algorithms. Given an index/key, for arrays is among
        the fastest structures when it comes to reading and writing that piece
        of memory.

        Note: do not confuse this with sequential/random/direct access data
        structuring. The above refers more specifically to direct indexing,
        whereas the latter refers to accessing a large blob/set of data, either
        in sequential or random order. 

        ---------------------------------
        |     Operation    | Complexity |
        ---------------------------------
        |   insert/del(1)  |    O(n)    |
        |   insert/del(n)  |    O(1)    |
        |   insert/del(i)  |    O(n)    |
        ---------------------------------
        Table 2. Insertion/Deletion complexities for arrays

        The above takes into account insert/deletion algorithms based on the
        index where the operation occurs at. Case A - insert/delete 1st element
        and Case C - insert/delete element at index i, where i is neither the
        first nor last element, will require every element AFTER index i to be
        pushed back or shifted forward, thus having the asymptotic complexity as
        stated. Case B - insert/delete at the end does not require any
        modifications to the existing elements of the arrays, hence O(1). Note
        that this algorithm requires an additional array of size N+1 to be created
        so space complexity is O(n).

        Note: because one can easily insert data into a random middle of an array,
        the array can become corrupted easily. 

        ------------------------------------
        |     Operation     |  Complexity  |
        ------------------------------------
        | Sequential search |     O(n)     |
        |   Binary search   |   O(log(n))  |
        ------------------------------------
        Table 3. Search algorithm time complexities

        Search algorithms for arrays are likely one of the significant cons of
        arrays as a data structure.

        Sequential search in python is implemented with the if ... in L. As such
        a binary search would be much more efficient.

    1.1.3 Sorting Algorithms

        Sorting algorithms share the goal of outputting a sorted list, but the
        way that each algorithm goes about this task can vary. When working with
        any kind of algorithm, it is important to know how fast it runs and in
        how much space it operates — in other words, its time complexity and
        space complexity.

        Additionally, sometimes stability may be an important factor in deciding
        the appropriate algorithm to use. A sorting algorithm is stable if it
        preserves the original order of elements with equal key values (where
        the key is the value the algorithm sorts by).

        -------------------------------------------------------------------------
        |   Operation    | Worse-case Comp. | Avg Comp.  | Space Comp. | Stable |
        -------------------------------------------------------------------------
        |   Merge sort   |    O(nlog(n))    | O(nlog(n)) |    O(n)     |    Y   |
        | Insertion sort |      O(n^2)      |   O(n^2)   |    O(1)     |    Y   |
        |  Bubble sort   |      O(n^2)      |   O(n^2)   |    O(1)     |    Y   |
        |   Quicksort    |      O(n^2)      | O(nlog(n)) |  log(n), n**|    N***|
        | Counting sort* |      O(k+n)      |   O(k+n)   |   O(k+n)    |    Y   |
        -------------------------------------------------------------------------
        Table 4. Sort algorithm complexities

        Reference source: https://brilliant.org/wiki/sorting-algorithms/

        * Radix sort as well
        ** O(log(n)) at best, O(n) on average
        *** Usually quicksort will result in unstable results, although there exists
        some stable implementations.

        Note that while heapsort applies for arrays, it will be discussed in
        the separate data structure instead. 


1.2 Heaps

    1.2.1 Background Information

        Heaps are a class of tree data structure that satisfies the heap property.
        If P is a parent node to C, then the key of P is either >= (max heap) or
        <= (min heap) that of C, where P and C applies to all nodes. In this, we
        will stick to the binary heap structure, so any log_2() will be denoted
        with log().

        A heap is a useful data structure when you need to repeatedly be removing
        objects of highest/lowest priority. This is possible due to heaps having
        a root node that can be easily accessed at the starting address of the
        data structure. HOWEVER, heaps are not designed to return an arbitrary
        element except for the max/min, a flaw in the data structure.

        Because a heap is essentially an array, access to elements have complexity
        of O(1).

        While an array can be used to implement the priority queue(PQ) ADT, heaps
        are the more common implementation. Basic operations of a PQ:
            1) insert(S,x) - insert element x into set S with some priority
            2) max(S) - return element of S with largest priority
                *in a max heap, the largest priority i.e the root is the max
                value of all elements in S => max(S) returns max valued element
            3) extract_max(S) - (2) + remove element from S

        -----------------------------------------------------------------------
        |    Operation    |      Array*      |    Binary Heap    |    BST**** |
        -----------------------------------------------------------------------
        |   insert(S,x)   |    O(n), O(1)    | O(1), O(log(n))** |  O(log(n)) |
        |      max(S)     |    O(1), O(n)    |       O(1)        |   O(1)***  |
        |  extract_max(S) |    O(1), O(n)    |     O(log(n))     |   O(1)***  |
        |   search(S,x)   |  O(log(n)), O(n) |       O(n)        |  O(log(n)) |
        |     create()    | O(nlog(n)), O(1) |       O(n)        | O(nlog(n)) |
        -----------------------------------------------------------------------
        Table 5. Comparing various data structures for implementing PQ ADT

        *Sorted array vs Unsorted array
        **Average complexity vs worse case complexity
        ***Using a trivially designed modifcation of a BST, it is possible to
        simulate a BST to get max keys like a heap, thus emulating heap's
        efficiency
        ****These are average complexity. Worse case comparison will be discussed
        in a later section on BSTs

        IMPORTANT NOTE: While complexity is an important factor in determining
        the appropriate algorithm, we cannot forget the multiple others out there
        such as (A) there can be same time complexity but different constant
        coefficients (B) ease of implementation (C) cache efficiency

        Useful reference:
            http://pages.cs.wisc.edu/~vernon/cs367/notes/PRIORITY-QAnswers.html
            https://stackoverflow.com/questions/6147242/heap-vs-binary-search-tree-bst/29548834#29548834
            (on comparing between binary heaps and balanced BSTs)
            
        Key properties of heaps as follows:
        
        A. Given an N element heap,
            1) No. of leaves = ceil(N/2)
            2) Indexes of leaves are (N/2+1, N/2+2, ... , N)
            3) Smallest possible depth/height = log(n)
            4) N = 2^h - 1, where h = height of tree, root being h=1
            for a copmlete binary tree. As such, if N = 2^k, for some
            integer k, then the height will have just increased
            5) To be exact, h = log(N+1). Since no operations are usually
            being done at the leaf level being the sub-tree's root, no. of
            steps usually required down the tree = h-1. Nevertheless,
            complexity can be approximated as log(N).
            
        B. Given a node of index i,
            1) index of left child = 2*i
            2) index of right child = 2*i + 1
            3) parent = floor(i/2)
            4) ALL OF THE ABOVE is assuming index 0 is ignored.
            If however index 0 is included, +1 to 1) and 2), floor(i-1/2) for 3)
    
    1.2.2 Basic Operations

        References:
            https://www.hackerearth.com/practice/notes/heaps-and-priority-queues/
            https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/MIT6_006F11_lec04.pdf
            
        1.2.2.1 max_heapify()

            This algorithm has a crucial criterion - given a node that possibly
            violates the max-heap property, its subtrees/children need to be
            max-heaps for max_heapify() algorithm to work correctly and logically.
            Only when the assumption is fulfilled, can we correct the violation
            by "trickling" the violated node down the tree to make the original
            node index i a max-heap.

            Complexity: O(log(n))
            
        1.2.2.2 build_maxheap()

            An important concept of this algorithm is the index i of the for loop.
            i begins with n/2, because as mentioned above, 1 to N/2 are the non-
            leaves of the heap. There is no necessity to run max_heapify() on
            leaves since they by definition fulfil the max-heap property. Also,
            i decreases rather than increases so as to exploit the assumption of
            max_heapify() and thus use it repeatedly.

            Complexity: O(n) upon careful analysis
            
        1.2.2.3 Min-heap variations

            This variation has an identical algorithm to max-heaps.
    
    1.2.3 Sorting Algorithms
    
       ------------------------------------------------------------------------
       |   Operation   | Worse-case Comp. | Avg Comp.  | Space Comp. | Stable |
        -----------------------------------------------------------------------
       |   Heap sort   |    O(nlog(n))    | O(nlog(n)) |  O(log(n))  |    N   |
       ------------------------------------------------------------------------
       Table 6. Various complexities of heap sort

       Space Complexity is O(log(n)) because while the only resource needed is a
       one-time array sized N creation. The recursive component of max_heapify
       causes the stack to expand proportionally to the height of the heap.

       ***Take note of this factor when determining space complexity of heaps,
       or even other recursive algorithms. Also if recursive algorithms can be
       written iteratively, the latter is always preferred in terms of space
       efficiency***

        Algorithm Process:
            1) Build a max-heap - O(n)
            2) Swap Arr[i] containing max key with Arr[N] - O(1)
            3) max_heapify(N-1) - O(log(n))
            4) Repeat sets 2 and 3 - repeat n times at worst

        Complexity: O(nlog(n))


1.3 Binary Search Trees (BST)

    1.3.1 Background Information

        BSTs are defined by the following structure - left sub-tree of a node
        has a key less than that of the parent's node, and right sub-tree being
        the reversed.        

        Insertion of elements into BSTs will always be at the leaf level.

        Obtaining access to a single element in the tree will require one to go
        through all the paths down the tree in sequence, leading to a complexity
        of O(h), where h is height of a node, taken as the longest path from the
        node down to the leaf. Only in the special case of a nearly balanced BST
        will h tend towards log(n) and O(h) = O(log(n)).

        Compared to heaps that are essentially arrays, BSTs are made up of pointers.
        As such, more bytes are needed per node of data. As such, results you get
        are pointers to the key values. 
    
    1.3.2 Basic Operations

        For some information on the complexities of basic operations, refer to
        Table 5.

       -------------------------------------------------
       |   Operation  | Worst-case Comp. |  Avg Comp.  |
        ------------------------------------------------
       |   search()   |       O(n)       |  O(log(n))  |
       |  ins()/del() |       O(n)       |  O(log(n))  |
       |   create()   |      O(n^2)      |  O(nlog(n)) |
       -------------------------------------------------
       Table 7. Comparing average and worst-case time complexities of BSTs

        Firstly, worst-case scenarios for BSTs all degenerate into a completely
        unbalanced tree i.e. a singly linked list, hence the complexities.

        Secondly, the average complexity considers a roughly balanced binary
        tree, and so asymptotic complexities can be roughly calculated this way.
        While it seems similar to a heap, unfortunately there is no detailed
        analysis on a lower bound. This, however, can be implemented using a
        self-balancing BST.
    
    1.3.3 Traversals

        Important traversals to be noted are (A) In-order (B) Pre-order (C) Post-
        order.

        Traversals are usually recursive and naturally have a space complexity
        of O(log(n)) or O(depth).

        A template for traversal algorithms is as such:
            Algo x(tree)
                1. x(left_sub_tree)
                2. get_root()
                3. x(right_sub_tree)
        where the sequence will vary.

        (A) In-order

            Algorithm sequence: 1,2,3
            Uses:
                1) produces nodes in sorted order
                2) checking the in-order traversal of 2 BSTs while rotating
                   will ensure that BST ordering is unchanged and thus they
                   are identical.
        
        (B) Pre-order

            Algorithm sequence: 2,1,3
            Uses: create copy of tree 
        
        (C) Post-order

            Algorithm sequence: 2,3,1
            Uses: delete tree


    1.3.4 Sort for BST
    
       ---------------------------------------------------------------
       |   Operation   | Worse-case Comp. | Avg Comp.  | Space Comp. |
        --------------------------------------------------------------
       |   Tree Sort   |       O(n)      |     O(n)    |     O(n)    |
       ---------------------------------------------------------------
       Table 8. The complexity of sort for BST

       Note the following that while a tree sort may seem more efficient than the
       usual O(nlog(n)) efficiency, keep in mind the complexity of creating
       a BST from given set of data i.e O(nlog(n)).

    1.3.5 Rotations

        Rotation is a tree operation primarily used for tree-balancing algorithms. 
        A summary on the specific instructions for each rotation is as follows:

        Single Rotations

        ---------------------------
        |            a            |
        |         /     \         |
        |        b        d       |
        |      /   \    /   \     |
        |     c     f  e     g    |
        ---------------------------
        Figure 1. Example of BST
        
            (A) Left-Rotation(x)

                1) From Figure 1, we perform Left-Rotation(a).
                2) d becomes the new root
                3) a takes ownership of d's left child as its right child
                4) d's left child becomes a
                
            (B) Right-Rotation(x)

                1) Now we perform Right-Rotation(a)
                2) b becomes the new root
                3) a takes ownership of b's right child as its left child
                4) b's left child becomes a

        Double Rotations
        
            (A) Left-Right-Rotation(x)

                1) Perform Right-Rotation(d)
                2) Perform Left-Rotation(a)
                
            (B) Right-Left-Rotation(x)

                1) Perform Left-Rotation(b)
                2) Perform Right-Rotation(a)

            
        Reference:
            https://www.cise.ufl.edu/~nemo/cop3530/AVL-Tree-Rotations.pdf

            *The above reference provides a clear case-by-case analysis on
            the distinct usage of individual rotations, as well as a complete
            pseudocode that determines which rotation instructions to use
            given a scenario.

    1.3.6 AVL Trees

        1.3.6.1 Data Structure Augmentation

            An AVL Tree is a classic example on the topic of 'Data Structure
            Augmentation'. This is simply put the process of taking an existing
            data structure, adding minor modifications/customisations whatever
            you call it, to fit the needs of your ADT.

            "For instance, let's say you start with a singly linked list, and you
            decide to add an additional node in one direction. You name the
            existing node left and the new node right. You also call the current
            node the parent of left and right. You end up with a binary tree"

            Reference:
            https://www.quora.com/What-are-the-uses-of-augmenting-data-structure

            Essentially, when performing DS Augmentation, the ultimate goal is
            to allow you to adjust the data structure to obtain a certain result
            at a greater efficiency, often at the cost of other results. This form
            of optimisation is useful when it comes to programs where one result
            is more frequently requested compared to another.

        1.3.6.2 Background Information

            AVL Tree is history's first self-balancing BST to be invented. In
            binary trees, the balance factor of a node N is defined to be the
            height difference between the left and the right subtrees of N.
            This is where the definition of AVLs come into play, where they are
            defined by their balance factor containing elements {-1,0,+1} being
            applied to each node N in the AVL tree.

        1.3.6.3 Code Reference

            Reference: https://gist.github.com/girish3/a8e3931154af4da89995

            Key algorithms are the 'insert', 'delete' and 'rebalance' algos.

        1.3.6.4 Self-balancing algorithm

            The process of rotation as mentioned earlier will inevitably modify
            the heights of various nodes. It is our intention to make full use
            of such an operation to improve overall efficiency of our program.

            Refer to rotations section for the same reference. This section will
            summarise with a pseudocode on when each of the 4 rotation techniques
            are used.

                IF tree is right heavy
                {
                     IF tree's right subtree is left heavy
                     {
                         Perform Double Left rotation
                     }
                     ELSE
                     {
                         Perform Single Left rotation
                     }
                }
                ELSE IF tree is left heavy
                {
                     IF tree's left subtree is right heavy
                     {
                         Perform Double Right rotation
                     }
                     ELSE
                     {
                         Perform Single Right rotation
                     }
                }

            Pseudocode 1. 4 different cases for balancing BSTs.


        1.3.6.5 Complexity and Efficiency

            Based on the worse case scenario calculation for AVLs, one can obtain
            the following relationship between the height h of an AVL tree and n,
            being the number of nodes.

                log(n+1) <= h < clog(n+2)+b,
                    where c = 1/log(golden_ratio),
                          b = clog(5)/2

            Similar to BSTs, the complexity for an insert/delete/search algorithm
            would have an average of O(log(n)), but even so for the worse case, as
            proven above. Of course, we must not forget the complexity of creating
            an AVL tree from given array of data compared to BSTs. Thankfully, AVL
            trees are considered to be a roughly balanced BST, as such, the
            complexity is O(nlog(n)), log(n) for each of the n keys. AVL trees have
            the additional rebalance() method that also take a scalar multiple of
            log(n) for each key, thus the asymptotic complexity will remain unchanged
            and identical. Better yet, the worst case complexity has improved to
            O(nlog(n)) too. 

            
