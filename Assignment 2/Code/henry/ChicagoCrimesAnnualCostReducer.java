import java.util.Iterator;
import java.io.IOException;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.mapreduce.Reducer;

public class ChicagoCrimesAnnualCostReducer extends Reducer<Text, DoubleWritable, Text, DoubleWritable>
{
    // DOMESTIC VIOLENCE [ value_list ]
    @Override
    protected void reduce(Text key, Iterable<DoubleWritable> values, Context context)throws IOException, java.lang.InterruptedException
    {

        double totalsum = 0;

        Iterator<DoubleWritable> valuesIter = values.iterator();

        /* For each store location */
        while (valuesIter.hasNext())
        {
            totalsum += valuesIter.next().get();
        }

        double totalAmount = totalsum;
        /* designation, average_increment */
        context.write(key, new DoubleWritable(totalAmount));
    }
}