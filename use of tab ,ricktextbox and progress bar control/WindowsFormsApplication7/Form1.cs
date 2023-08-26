using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication7
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
           //tabcontrol use 
            textBox2.Text = textBox1.Text;

            //use of progress bar
             for (int i=0; i<= 100; i++)
            {
                progressBar1.PerformStep();
            }
            //use of richtextbox control
             richTextBox1.ZoomFactor = (int)numericUpDown1.Value;
             textBox1.Text = "";
             MessageBox.Show("Saved");
        }

        

      

    }
}
