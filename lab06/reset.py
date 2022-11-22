import sysv_ipc

key = 12

try:
    sem1 = sysv_ipc.Semaphore(key, sysv_ipc.IPC_CREX, 0o700, 0)
    sem2 = sysv_ipc.Semaphore(key + 1, sysv_ipc.IPC_CREX, 0o700, 1)
    mem = sysv_ipc.SharedMemory(key, sysv_ipc.IPC_CREX)

except sysv_ipc.ExistentialError:
    sem1 = sysv_ipc.Semaphore(key)
    sem2 = sysv_ipc.Semaphore(key + 1)
    mem = sysv_ipc.SharedMemory(key)

sysv_ipc.remove_shared_memory(mem.id)
sysv_ipc.remove_semaphore(sem1.id)
sysv_ipc.remove_semaphore(sem2.id)
