using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication10
{
    public partial class Form3 : Form
    {
        public Form3()
        {
            InitializeComponent();
        }

        

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (progressBar1.Value == 100)
            {
                Form4 f2 =new Form4();
                f2.Show();
                timer1.Stop();
                this.Close();

            }
            else
            {
                progressBar1.Value = progressBar1.Value + 1;
                    label1.Text=progressBar1.Value + "% Completing....";
            }


        }

      
       
        private void Form3_Load(object sender, EventArgs e)
        {
            timer1.Start();
        }
    }
}
