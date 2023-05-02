public class PartialPivoting{
    public static void main(String[] args){

        // Creates a random matrix of size MxN with random numbers 0-1 inside them. 
        double[][] Q1B = new double[100][10];
        createMatrix(Q1B);
        System.out.println("The matrix 100x10 after row reduction is shown here: \n");
        rowReduction(Q1B);
        printMatrix(Q1B);
        
        double[][] Q2B5x5 = new double[5][5];
        createMatrix(Q2B5x5);
        System.out.println("\nFor a matrix 5x5 to be row reduced");  
        printTimeTaken(Q2B5x5);
  
        
        double[][] Q2B50x50 = new double[50][50];
        createMatrix(Q2B50x50);
        System.out.println("\nFor a matrix 50x50 to be row reduced");
        printTimeTaken(Q2B50x50);
        
        double[][] Q2B500x500 = new double[500][500];
        createMatrix(Q2B500x500);
        System.out.println("\nFor a matrix 500x500 to be row reduced");
        printTimeTaken(Q2B500x500);  
   
    }
    public static void rowReduction(double[][] coEff){
        for(int numPivots = 0; numPivots <coEff[0].length - 1; numPivots++){
            int rowValue = numPivots;
            //Checks for the value in a column that is the largest. 
            for(int i = numPivots; i < coEff.length; i++){
                if(Math.abs(coEff[i][numPivots]) > Math.abs(coEff[rowValue][numPivots]))
                    rowValue = i;
                }
                //Upon finding the largest value, swap rows to the correct pivot row position. 
                swapRow(coEff, rowValue, numPivots);
                columnEliminate(coEff, numPivots);
            }
    }
    
    //swaps two rows
    public static void swapRow(double[][] coEff, int rowValue, int numPivots){
        for(int i = 0; i < coEff[rowValue].length; i++){
            double tempValue = coEff[numPivots][i];
            coEff[numPivots][i] = coEff[rowValue][i];
            coEff[rowValue][i] = tempValue;
        }
    }

    //Acts to eliminate all row values in a column below the pivot. 
    public static void columnEliminate(double[][] coEff, int numPivots){
        for(int i = numPivots + 1; i < coEff.length; i++){
            double multiplier = coEff[i][numPivots] / coEff[numPivots][numPivots];
            for(int j = 0; j < coEff[i].length; j++){
                coEff[i][j] = coEff[i][j] - (multiplier * coEff[numPivots][j]);
            }
        }
    }

    //easier way to print matrix and see it
    public static void printMatrix(double[][] coEff){
        for (int i = 0; i < coEff.length; i++) {
            for(int j = 0; j < coEff[i].length; j++){
                System.out.printf("%.2f ", coEff[i][j]);
        }
        System.out.println();
    }
    }
    
    //Utilizes Math.random to fill matrices with numbers
    public static void createMatrix(double[][]A){
      for(int i = 0; i < A.length; i++){
         for(int j = 0; j < A[i].length; j++){
            A[i][j] = (Math.random());
           }
        }
    }
    
    //a timer to check the time complexity for Question 2b.
    public static void printTimeTaken(double[][]A){
        long startTime = System.nanoTime();
        rowReduction(A);
        long endTime = System.nanoTime();
        System.out.println("That took " + (endTime - startTime) + " nanoseconds");
    }
 }
    