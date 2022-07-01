import java.rmi.Remote;
import java.rmi.RemoteException;

public interface RmiInterfaceRemotaJava extends Remote {

    boolean validarCPF(String cpf) throws RemoteException;

}
