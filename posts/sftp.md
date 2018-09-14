

usermod -s /sbin/nologin



/etc/sshd/sshd_conf 

```



Subsystem      sftp    internal-sftp



Match User netsupport24

        X11Forwarding no

        AllowTcpForwarding no

        AllowAgentForwarding no

        PermitTunnel no

        ForceCommand internal-sftp

        ChrootDirectory /usr/local/lsws

```