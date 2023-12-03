package day1;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;


public class Main {
    private static final Map<String, String> WORD_TO_ALPHANUMERIC = new HashMap<>();

    static {
        WORD_TO_ALPHANUMERIC.put("one", "o1e");
        WORD_TO_ALPHANUMERIC.put("two", "t2o");
        WORD_TO_ALPHANUMERIC.put("three", "t3e");
        WORD_TO_ALPHANUMERIC.put("four", "f4r");
        WORD_TO_ALPHANUMERIC.put("five", "f5e");
        WORD_TO_ALPHANUMERIC.put("six", "s6x");
        WORD_TO_ALPHANUMERIC.put("seven", "s7n");
        WORD_TO_ALPHANUMERIC.put("eight", "e8t");
        WORD_TO_ALPHANUMERIC.put("nine", "n9e");
    }

    public static void main(String[] args) {
        if (args.length == 0) {
            System.out.println("Usage: java Main <file_path>");
            return;
        }

        String filePath = args[0];

        try {
            String originalText = readFile(filePath);

            int originalCalibration = calculateCalibration(originalText);
            System.out.println("Original Calibration: " + originalCalibration);

            String modifiedText = replaceNumberWords(originalText);
            int modifiedCalibration = calculateCalibration(modifiedText);
            System.out.println("Modified Calibration: " + modifiedCalibration);
        } catch (IOException e) {
            System.err.println("Error reading the file: " + e.getMessage());
        }
    }

    private static String readFile(String filePath) throws IOException {
        StringBuilder content = new StringBuilder();
        try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = reader.readLine()) != null) {
                content.append(line).append("\n");
            }
        }
        return content.toString();
    }

    private static String replaceNumberWords(String text) {
        for (Map.Entry<String, String> entry : WORD_TO_ALPHANUMERIC.entrySet()) {
            text = text.replace(entry.getKey(), entry.getValue());
        }
        return text;
    }

    private static int calculateCalibration(String text) {
        String[] lines = text.replaceAll("[A-z]", "").split("\n");
        int sum = 0;
        for (String line : lines) {
            sum += Integer.parseInt(String.valueOf(line.charAt(0)) + line.charAt(line.length() - 1));
        }
        return sum;
    }
}
