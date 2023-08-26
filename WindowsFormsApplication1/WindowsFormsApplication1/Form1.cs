using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int a, b, c, d, g ,f, sum1,sum2;
            float per1, per2;
            a = Convert.ToInt16(textBox1.Text);
            b = Convert.ToInt16(textBox2.Text);
            c = Convert.ToInt16(textBox3.Text);
            d = Convert.ToInt16(textBox4.Text);
            g = Convert.ToInt16(textBox5.Text);
            f = Convert.ToInt16(textBox6.Text);

            sum1 = a + b + c;
            sum2 = d + g + f;
            per1 = sum1 / 3;
            per2 = sum2 / 3;
            textBox7.Text = Convert.ToString(sum1);
            textBox9.Text = Convert.ToString(per1);
            if (per1 < 30)
            {
                label4.Text = "Student1 is FAIL";
            }
            else if (per1 > 30 && per1 < 60)
            {
                label4.Text = "Student1 is Average";
            }
            else
            {
                label4.Text = "Student1 is Good";
            }


            textBox8.Text = Convert.ToString(sum2);
            textBox10.Text = Convert.ToString(per2);
            if (per2 < 30)
            {
                label5.Text = "Student2 is FAIL";
            }
            else if (per2 > 30 && per2 < 60)
            {
                label5.Text = "Student2 is Average";
            }
            else
            {
                label5.Text = "Student2 is Good";
            }
        }

        
    }
}
