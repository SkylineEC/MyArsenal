package day03;

import day01.Array;

import java.util.ArrayList;
import java.util.Scanner;

public class StudentOrganize {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<Student> stuList = new ArrayList<>();

        while (true) {

            System.out.println("------欢迎使用学生管理系统------");
            System.out.println("输入1，添加学生信息");
            System.out.println("输入2，展示所有学生信息");
            System.out.println("输入3，删除学生信息");
            System.out.println("输入4，修改学生信息");
            System.out.println("输入5，退出系统");

            int function = sc.nextInt();
            switch (function) {
                // 添加学生
                case 1: {
                    System.out.println("-----添加新的学生名单！-----");
                    stuList.add(addStudent());
                    break;
                }
                //展示所有学生
                case 2: {
                    System.out.println("-----全部学生信息-----");
                    showAllStudent(stuList);
                    break;
                }
                //删除学生
                case 3: {
                    break;
                }

                //修改学生信息
                case 4: {
                    break;
                }
                //退出系统
                case 5: {
                    System.out.println("-----谢谢使用------");
                    System.exit(0);
                }

            }
        }
    }

    //1添加学生
    public static Student addStudent() {
        Student stu = new Student();
        Scanner sc = new Scanner(System.in);

        System.out.println("请输入学生的学号：");
        stu.setStuID(sc.nextLine());

        System.out.println("请输入学生的姓名：");
        stu.setName(sc.nextLine());

        System.out.println("请输入学生的年龄：");
        stu.setAge(sc.nextInt());

        System.out.println("请输入学生的地址：");
        stu.setAddress(sc.nextLine());

        System.out.println("-----学生录入成功!-----");
        return stu;
    }

    //2展示所有学生
    public static void showAllStudent(ArrayList<Student> array) {
        for (int i = 0; i < array.size(); i++) {
            System.out.println(array.get(i).getStuID() + "\t" + array.get(i).getName() + "\t" + array.get(i).getAge() + "\t" + array.get(i).getAddress());
        }
    }

    //移除学生
    public static Student removeStudent(ArrayList<Student> array, Student stu) {
        return stu;

    }


}