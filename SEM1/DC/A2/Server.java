package test;
import java.net.*;
import java.io.*;
public class Server {
  public static void main(String args[]) throws IOException {
	//Port number can be from 0 to 65535,provide same port at the client.
    ServerSocket s = new ServerSocket(1001);
    //ServerSocket is again a Socket with additional features of server end point,
    //It is created to bind to a port and listen for a connect from a client.
    System.out.println("Server Connected...\n");
    System.out.println("Server Started...\n");
    System.out.println("Waiting for a client...\n");
    Socket s1=s.accept(); 
    // accept() method blocks until a client connects to the server.
    System.out.println("\nClient accepted");
    OutputStream os = s1.getOutputStream();
    DataOutputStream dos= new DataOutputStream (os);
    dos.writeUTF("Connection Accepted Successfully......");
    //writeUTF:Writes a string to the underlying output stream using 
  	//modified UTF-8 encoding in a machine independent manner.
	InputStream is = s1.getInputStream();
    BufferedReader br= new BufferedReader(new InputStreamReader(is));
	String message= br.readLine();
	System.out.println(message);
	s.close();
  }
}
//socket the one point for the two way communication between the process