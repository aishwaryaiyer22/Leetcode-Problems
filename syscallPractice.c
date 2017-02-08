#include <linux/unistd.h>
//blah blah

// in file kernel/include/uapi/asm-generic/unistd:
#define __NR_pinfo 245
__SYSCALL(__NR_pinfo, sys_pinfo)

//in file kernel/include/linux/syscalls.h
asmlinkage long sys_pinfo(struct proc_struct ___user* proc, pid_t pid);

//in pinfo.c in kernel/kernel

SYSCALL_DEFINE1(pinfo,struct proc_struct, proc, int, pid) {
	
	retval = -EINVAL
	struct task_struct *t; 
	struct proc_struct *tmp_proc;
	if (proc_struct == NULL)
		return -EINVAL;
	if(pid < 0)
		return retval;
	rcu_read_lock();
	t = get_task_by_vpid(pid);

	if(!t){
		rcu_read_unlock();
		return -ESRCH;
	}	
	tmp_proc->pid = t->cred->uid;
	rcu_read_unlock();

	if(copy_to_user(proc, tmp_proc, struct proc_struct) != 0)
		return -EFAULT
	return 0
}

//user space code
int main(int argc, char** argv) {
	struct proc_struct * proc_result;
	pid_t pid;
	int result;

	if (argc != 2)
		printf("oops");
	pid = (int)strtol(argv[1], NULL, 10);
	result = syscall(__NR_pinfo, pid);
	if (result == 0)
		print ("pid %u parent pid %u nice %ld", proc_result->pid, proc_result->ppid, proc_result->nice);


}

int main(int argc, char** argv) {
	int fds[2], fold;
	char** command = "/bin/ls | /bin/grep h"
}