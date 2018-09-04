import java.util.HashMap;
import java.io.FileReader;
import java.io.IOException;
import java.io.BufferedReader;

import org.apache.hadoop.filecache.DistributedCache;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.io.DoubleWritable;

public class ChicagoCrimesAnnualCostMapper extends Mapper<LongWritable, Text, Text, DoubleWritable>
{

    private HashMap<String, Double> cost_map = new HashMap<String, Double>();      // [ [ {cost: 31286} {....} {....} ] ]

    @Override
    protected void setup(Context context) throws IOException, InterruptedException
    {
        /* read data from distributed cache */
        BufferedReader br = null;
        Path[] LocalfilesPath = DistributedCache.getLocalCacheFiles(context.getConfiguration());
        String record = "";

        for (Path path : LocalfilesPath)
        {
            if (path.getName().toString().trim().equals("cost.txt"))
            {
                br = new BufferedReader(new FileReader(path.toString()));
                record = br.readLine();          // cost,31286
                while (record != null)
                {
                    String data[] = record.split(",");                 //   [ {cost} {31286}]
                    /* store the values from the cache file in the has map
                     * In this case every crime type may have a different inmate cost per year
                      * but I decide to use a common figure cited from the article whose link has been provided*/
                    cost_map.put(data[0].trim(), Double.parseDouble(data[1].trim()));
                    record = br.readLine();
                }
            }
        }
    }

    @Override
    // DOMESTIC VIOLENCE,1
    protected void map(LongWritable key, Text value,  Context context)throws IOException, java.lang.InterruptedException
    {

        String line = value.toString();
        /* Split csv string */
        String[] words = line.split(",");                         //  [{DOMESTIC VIOLENCE} {1}]

        String crimeType= words[0] ;         //  crimeType = DOMESTIC VIOLENCE

        double amount = 0;
        if (crimeType.toString().equalsIgnoreCase("DOMESTIC VIOLENCE"))
        {
            amount = cost_map.get("cost");       // n= 31286
        }
        else if(crimeType.toString().equalsIgnoreCase("RITUALISM"))
        {
            amount = cost_map.get("cost");       // n= 31286
        }
        else if(crimeType.toString().equalsIgnoreCase("NON-CRIMINAL (SUBJECT SPECIFIED)"))
        {
            amount = cost_map.get("cost");       // n= 31286
        }
        else if(crimeType.toString().equalsIgnoreCase("NON - CRIMINAL"))
        {
            amount = cost_map.get("cost");       // n= 31286
        }
        else if(crimeType.toString().equalsIgnoreCase("HUMAN TRAFFICKING"))
        {
            amount = cost_map.get("cost");       // n= 31286
        }
        else if(crimeType.toString().equalsIgnoreCase("NON-CRIMINAL"))
        {
            amount = cost_map.get("cost");       // n= 31286
        }
        else if(crimeType.toString().equalsIgnoreCase("OTHER NARCOTIC VIOLATION"))
        {
            amount = cost_map.get("cost");       // n= 31286
        }
        else if(crimeType.toString().equalsIgnoreCase("PUBLIC INDECENCY"))
        {
            amount = cost_map.get("cost");       // n= 31286
        }
        else if(crimeType.toString().equalsIgnoreCase("CONCEALED CARRY LICENSE VIOLATION"))
        {
            amount = cost_map.get("cost");       // n= 31286
        }
        else if(crimeType.toString().equalsIgnoreCase("OBSCENITY"))
        {
            amount = cost_map.get("cost");       // n= 31286
        }
        else if(crimeType.toString().equalsIgnoreCase("STALKING"))
        {
            amount = cost_map.get("cost");       // n= 31286
        }
        else if(crimeType.toString().equalsIgnoreCase("INTIMIDATION"))
        {
            amount = cost_map.get("cost");       // n= 31286
        }
        else if(crimeType.toString().equalsIgnoreCase("KIDNAPPING"))
        {
            amount = cost_map.get("cost");       // n= 31286
        }
        else if(crimeType.toString().equalsIgnoreCase("ARSON"))
        {
            amount = cost_map.get("cost");       // n= 31286
        }
        else if(crimeType.toString().equalsIgnoreCase("CRIM SEXUAL ASSAULT"))
        {
            amount = cost_map.get("cost");       // n= 31286
        }
        else if(crimeType.toString().equalsIgnoreCase("HOMICIDE"))
        {
            amount = cost_map.get("cost");       // n= 31286
        }
        else if(crimeType.toString().equalsIgnoreCase("SEX OFFENSE"))
        {
            amount = cost_map.get("cost");       // n= 31286
        }
        else if(crimeType.toString().equalsIgnoreCase("OFFENSE INVOLVING CHILDREN"))
        {
            amount = cost_map.get("cost");       // n= 31286
        }
        else if(crimeType.toString().equalsIgnoreCase("INTERFERENCE WITH PUBLIC OFFICER"))
        {
            amount = cost_map.get("cost");       // n= 31286
        }
        else if(crimeType.toString().equalsIgnoreCase("LIQUOR LAW VIOLATION"))
        {
            amount = cost_map.get("cost");       // n= 31286
        }
        else if(crimeType.toString().equalsIgnoreCase("GAMBLING"))
        {
            amount = cost_map.get("cost");       // n= 31286
        }
        else if(crimeType.toString().equalsIgnoreCase("BURGLARY"))
        {
            amount = cost_map.get("cost");       // n= 31286
        }
        else if(crimeType.toString().equalsIgnoreCase("ROBBERY"))
        {
            amount = cost_map.get("cost");       // n= 31286
        }
        else if(crimeType.toString().equalsIgnoreCase("MOTOR VEHICLE THEFT"))
        {
            amount = cost_map.get("cost");       // n= 31286
        }
        else if(crimeType.toString().equalsIgnoreCase("PUBLIC PEACE VIOLATION"))
        {
            amount = cost_map.get("cost");       // n= 31286
        }
        else if(crimeType.toString().equalsIgnoreCase("DECEPTIVE PRACTICE"))
        {
            amount = cost_map.get("cost");       // n= 31286
        }
        else if(crimeType.toString().equalsIgnoreCase("CRIMINAL DAMAGE"))
        {
            amount = cost_map.get("cost");       // n= 31286
        }
        else if(crimeType.toString().equalsIgnoreCase("WEAPONS VIOLATION"))
        {
            amount = cost_map.get("cost");       // n= 31286
        }
        else if(crimeType.toString().equalsIgnoreCase("PROSTITUTION"))
        {
            amount = cost_map.get("cost");       // n= 31286
        }
        else if(crimeType.toString().equalsIgnoreCase("OTHER OFFENSE"))
        {
            amount = cost_map.get("cost");       // n= 31286
        }
        else if(crimeType.toString().equalsIgnoreCase("ASSAULT"))
        {
            amount = cost_map.get("cost");       // n= 31286
        }
        else if(crimeType.toString().equalsIgnoreCase("CRIMINAL TRESPASS"))
        {
            amount = cost_map.get("cost");       // n= 31286
        }
        else if(crimeType.toString().equalsIgnoreCase("THEFT"))
        {
            amount = cost_map.get("cost");       // n= 31286
        }
        else if(crimeType.toString().equalsIgnoreCase("BATTERY"))
        {
            amount = cost_map.get("cost");       // n= 31286
        }
        else if(crimeType.toString().equalsIgnoreCase("NARCOTICS"))
        {
            amount = cost_map.get("cost");       // n= 31286
        }
        else
        {
            System.out.println("Invalid designation");
        }

        int noOfCrimes = Integer.parseInt(words[1].trim());
        double totalAmountPerCrime = amount*noOfCrimes;

        context.write(new Text(crimeType), new DoubleWritable(totalAmountPerCrime));
    }
}