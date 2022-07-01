import java.io.File;
import java.nio.file.Files;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.Base64;

import javax.swing.JOptionPane;

public class RmiClienteJava {

    public static void main(String[] args) {
        try {
            // localiza o registro
            // obtém o stub para o registro
            Registry registry = LocateRegistry.getRegistry("127.0.0.1", 1099);

            // localiza o serviço registrado como AbcBolinhas
            RmiInterfaceRemotaJava stub = (RmiInterfaceRemotaJava) registry.lookup("AbcBolinhas");

            System.out.println("<<<<< teste função valida cpf() >>>>>>>>>");
            System.out.println(stub.validarCPF("08860883997"));
            

        } catch (Exception e) {
            System.err.println("!Erro no cliente: " + e.toString());
        }
    }
}


//essa instrução deixa a sessão do shell em UTF-8
//chcp 65001

//essa deixa em Win1252 (padrão do cmd do windows)
//chcp 1252

