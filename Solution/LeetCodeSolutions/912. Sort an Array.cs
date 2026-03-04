namespace SortAnArray
{
    class Solution
    {
        public static int[] SortArray(int[] array)
        {
            for (int i = 1; i < array.Length; i++)
            {
                int j = i - 1;
                int k = array[i];

                while (j >= 0 && k < array[j])
                {
                    array[j + 1] = array[j];
                    j -= 1;
                }

                array[j + 1] = k;
            }

            foreach (int num in array)
            {
                Console.WriteLine($"{num}");
            }

            return array;
        }

        public static int Main()
        {
            int[] array2 = [5, 1, 1, 2, 0, 0];
            SortArray(array2);

            return 1;
        }
    }
}
