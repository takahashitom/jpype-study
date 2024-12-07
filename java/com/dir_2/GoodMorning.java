package com.dir_2;

public class GoodMorning{
    private String message;

    public GoodMorning(String message){
        this.message = message;
    }

    public String sendMorning(){
        String result = "Good Morning " + this.message;
        return result;
    }
}