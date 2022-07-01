import java.io.File;
import java.io.FileOutputStream;
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;
import java.util.Arrays;
import java.util.Base64;
import java.util.Random;

import java.util.Scanner;
import static java.lang.Math.toIntExact;

public class RmiServidorJava implements RmiInterfaceRemotaJava {

    // Implementação dos métodos da interface que podem ser invocados remotamente

    //para iniciar a validação marque como true
    public boolean validarCPF(String cpf) throws RemoteException {  
    cpf = cpf.replace(".", "");
    cpf = cpf.replace("-", "");
    
    try{
      Long.parseLong(cpf);
    } catch(NumberFormatException e){
      return false;
    }

    int d1, d2;
    int digito1, digito2, resto;
    int digitoCPF;
    String nDigResult;

    d1 = d2 = 0;
    digito1 = digito2 = resto = 0;

    for (int nCount = 1; nCount < cpf.length() - 1; nCount++) {
      digitoCPF = Integer.valueOf(cpf.substring(nCount - 1, nCount)).intValue();

      // multiplique a ultima casa por 2 a seguinte por 3 a seguinte por 4
      // e assim por diante.
      d1 = d1 + (11 - nCount) * digitoCPF;

      // para o segundo digito repita o procedimento incluindo o primeiro
      // digito calculado no passo anterior.
      d2 = d2 + (12 - nCount) * digitoCPF;
    };

    // Primeiro resto da divisão por 11.
    resto = (d1 % 11);

    // Se o resultado for 0 ou 1 o digito é 0 caso contrário o digito é 11
    // menos o resultado anterior.
    if (resto < 2)
      digito1 = 0;
    else
      digito1 = 11 - resto;

    d2 += 2 * digito1;

    // Segundo resto da divisão por 11.
    resto = (d2 % 11);

    // Se o resultado for 0 ou 1 o digito é 0 caso contrário o digito é 11
    // menos o resultado anterior.
    if (resto < 2)
      digito2 = 0;
    else
      digito2 = 11 - resto;

    // Digito verificador do CPF que está sendo validado.
    String nDigVerific = cpf.substring(cpf.length() - 2, cpf.length());

    // Concatenando o primeiro resto com o segundo.
    nDigResult = String.valueOf(digito1) + String.valueOf(digito2);

    // comparar o digito verificador do cpf com o primeiro resto + o segundo
    // resto.
    return nDigVerific.equals(nDigResult);
  }



    public static void main(String args[]) {
        try {
            RmiServidorJava obj = new RmiServidorJava();

            // Importante: não tirar o "0" do segundo argumento do método exportObject
            // Se não a JVM não gera o stub automaticamente e buscara um ServidorRMI_stub.class em tempo de execução.
            // Nesse caso teria que ser utilizado o rmic para gerar a ServidorRMI_stub.class
            // Maiores detalhes em: http://java.sun.com/j2se/1.5.0/docs/guide/rmi/relnotes.html
            // Exporta o objeto remoto colocando-o em listening para receber request numa
            // porta anônima TCP - retorna o stub do objeto servidor
            RmiInterfaceRemotaJava stub = (RmiInterfaceRemotaJava) UnicastRemoteObject.exportObject(obj, 0);
            String refRemota = stub.toString();
            System.out.println("Stub Gerado: " + refRemota.substring(refRemota.indexOf("endpoint")));

            // Tenta localizar o rmiregistry no host local na porta default (1099), caso não
            // encontre, retorna erro: RemoteException
            Registry registro = LocateRegistry.createRegistry(1099);
            refRemota = registro.toString();
            System.out.println("Registro: " + refRemota.substring(refRemota.indexOf("endpoint")));

            // Registra o objeto servidor através de um nome "AbcBolinhas" e de sua interface "stub"
            // Se o string AbcBolinhas já estiver associado a outro objeto remoto, ocorre uma exceção
            registro.rebind("AbcBolinhas", stub);

        } catch (Exception e) {
            System.out.println("Erro no servidor:" + e.getMessage());
        }
    }

}