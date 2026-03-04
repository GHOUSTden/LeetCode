namespace LeetCodeSolutions
{
    internal class MySort
    {
        public static int[] InsertionSort(int[] array) 
        {
            int[] a = new int[array.Length];

            for (int i = 1; i < array.Length; i++)
            {
                int j = i - 1;
                int k = array[i];

                while (j >= 0 && k < array[j])
                {
                    array[j + 1] = array[j];
                    j -= 1;
                }

                a[j + 1] = k;
            }

            return a;
        }
    }
}
