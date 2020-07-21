package com.example.android.stayhealthy;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

public class InfoActivity extends AppCompatActivity {

    TextView pneumonia,pneumoniaDescription,instruction,instructionDescription;
    boolean pvis=false,ivis=false;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_info);

        getSupportActionBar().setTitle("Info");

        pneumonia=(TextView)findViewById(R.id.pneumonia);
        pneumoniaDescription=(TextView)findViewById(R.id.pneumonia_description);
        instruction=(TextView)findViewById(R.id.instruction);
        instructionDescription=(TextView)findViewById(R.id.instruction_description);

        pneumonia.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(pvis){
                    pvis=false;
                    pneumoniaDescription.setVisibility(View.GONE);
                }else{
                    pvis=true;
                    pneumoniaDescription.setVisibility(View.VISIBLE);
                }
            }
        });

        instruction.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(ivis){
                    ivis=false;
                    instructionDescription.setVisibility(View.GONE);
                }else{
                    ivis=true;
                    instructionDescription.setVisibility(View.VISIBLE);
                }
            }
        });
    }
}