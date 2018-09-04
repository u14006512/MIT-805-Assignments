import java.io.IOException;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

import org.apache.hadoop.filecache.DistributedCache;
import java.net.URI;
import java.net.URISyntaxException;

public class ChicagoCrimesAnnualCost
{

    public static void main(String[] args) throws IOException, ClassNotFoundException, InterruptedException,URISyntaxException
    {

        // these path are hard coded using my file system
        Path inputPath = new Path("/home/henry/Documents/hadoop-1.2.1/HadoopProjects/chicago/inputs/crimes.txt");
        Path outputDir = new Path("/home/henry/Documents/hadoop-1.2.1/HadoopProjects/chicago/output/");

        Configuration conf = new Configuration();
        // add files to cache
        DistributedCache.addCacheFile(new URI("/home/henry/Documents/hadoop-1.2.1/HadoopProjects/chicago/inputs/cost.txt"), conf);

        Job job = new Job(conf, "Chicago Crimes Annual Cost");

        //name of driver class
        job.setJarByClass(ChicagoCrimesAnnualCost.class);
        //name of Mapper class
        job.setMapperClass(ChicagoCrimesAnnualCostMapper.class);
        //name of Reducer class
        job.setReducerClass(ChicagoCrimesAnnualCostReducer.class);

        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(DoubleWritable.class);

        FileInputFormat.addInputPath(job, inputPath);
        FileOutputFormat.setOutputPath(job, outputDir);

        outputDir.getFileSystem(job.getConfiguration()).delete(outputDir,true);

        job.waitForCompletion(true);
    }
}
