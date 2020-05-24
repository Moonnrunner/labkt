import java.net.*;

public class URLDepthPair {

    private int currentDepth; //Поле для текущей глубины
    private String currentURL;//Поле для текущего URL

    //Конструктор для глубины и URL
    public URLDepthPair(String URL, int depth){
        currentDepth = depth;
        currentURL = URL;
    }
    //Метод, который возвращает текущий URL
    public String getURL() {
        return currentURL;
    }
    //Метод, который возвращает текущую глубину
    public int getDepth() {
        return currentDepth;
    }
    //Метод, который возвращает текущий URL и текущую глубину в строке
    public String toString() {
        String stringDepth = Integer.toString(currentDepth);
        return stringDepth + '\t' + currentURL;
    }
    //Метод который возвращает docPath текущий URL 
    public String getDocPath() {
        try {
            URL url = new URL(currentURL);
            return url.getPath();
        }
        catch (MalformedURLException e) {
            System.err.println("MalformedURLException: " + e.getMessage());
            return null;
        }
    }
    //Метод который возвращает WebHost текущий URL 
    public String getWebHost() {
        try {
            URL url = new URL(currentURL);
            return url.getHost();
        }
        catch (MalformedURLException e) {
            System.err.println("MalformedURLException: " + e.getMessage());
            return null;
        }
    }  
}