/*
    Author: Shaik Faizan Roshan Ali
    Date: 29th May 2022
    Description: This is the implementation of Union & Find operation on disjoint sets.
                 (Without path compression)
**/

import java.util.Vector;
public class UnionFind {
    
    /*
    
        Parent array is used for keeping track of the parent for each node
        Rank determines the rank of the set
        setSize determines the size of the set.
        numSets determines the number of sets.
    **/
    Vector<Integer> parent, rank, setSize;
    int numSets;
    UnionFind(int n) {
        
        parent = new Vector<Integer>(n);
        rank = new Vector<Integer>(n);
        setSize = new Vector<Integer>(n);
        numSets = n;
        
        for(int i = 0; i < n; i++) {
            
            parent.add(i);
            rank.add(0);
            setSize.add(1);
        }
    }
    
    /* findset method is used to check to which set the node belongs to */
    public int findSet(int i) {
        
        if(parent.get(i) == i) {
            
            return i;
        }
        
        else {
            
            int papa = findSet(parent.get(i));
            parent.set(i, papa); // maybe path compression
            return papa;
        }
    }
    
    /* Union is used for performing union of two disjoint sets */
    public void union(int i, int j) {
        
        int parent1 = findSet(i);
        int parent2 = findSet(j);
        
        /* union is only possible if the parent/root of both nodes are different */
        if(parent1 != parent2) {
            
            numSets--;
            if(rank.get(parent1) > rank.get(parent2)) {
                
                parent.set(parent2, parent1); // cause parent 1 rank is higher
                setSize.set(parent1, setSize.get(parent1) + setSize.get(parent2));
                
                /* rank doesn't change in this scenario */
            }
        
            else {
                
                parent.set(parent1, parent2);
                setSize.set(parent2, setSize.get(parent1)+ setSize.get(parent2));
                
                if(rank.get(parent1) == rank.get(parent2)) {
                    
                    rank.set(parent2, rank.get(parent2)+1);
                }
            }        
        }
        
    }  
    
    
    public static void main(String args[]) {
        
        /* Sample test case for reference*/
        UnionFind uf = new UnionFind(5);
        
        System.out.println("4 belongs to set : " + uf.findSet(4));
        uf.union(4, 3); /* Parent of 4 is set as 3*/
        System.out.println("4 belongs to set : " + uf.findSet(4));
        uf.union(4, 2); /* Parent of 2 is set as 4 */
        System.out.println("2 belongs to set : " + uf.findSet(2));
        uf.union(1, 4); /* Parent of 1 is set as 4 */
        System.out.println("1 belongs to set : " + uf.findSet(1));
    }
}
