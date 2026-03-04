class Solutions
{
    public static int HeightChecker(int[] heights)
    {
        int noi = 0;
        int[] expected = new int[heights.Length];

        Array.Copy(heights, expected, heights.Length);

        LeetCodeSolutions.MySort.InsertionSort(expected);

        for (int i = 0; i < expected.Length; i++)
        {
            if (heights[i] != expected[i])
            {
                noi++;
            }
        }

        Console.WriteLine(noi);

        return noi;
    }

    public static int Main()
    {
        int[] heights = [1, 1, 4, 2, 1, 3];
        HeightChecker(heights);

        return 1;
    }
}