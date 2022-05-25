using System;
using System.IO;

namespace StockBattle
{
    class Market
    {
        public void print ()
        {
            Log();
            Console.WriteLine("have now logged");
        }

        public async void Log()
        {
            DateTime dt = DateTime.Now;
            string lines = $"{dt}: First line";

            using StreamWriter file = new(@".\logs\market.log", append: true);
            await file.WriteLineAsync(lines);
        }
    }
}