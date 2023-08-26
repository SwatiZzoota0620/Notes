using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int num,factorial,i;
            num = Convert.ToInt16(textBox1.Text);
          
           factorial = 1;
            if (num < 0)
            {
                MessageBox.Show("Sorry, factorial does not exist for negative numbers");
            }
            else if (num == 0)
            {
                MessageBox.Show("The factorial of 0 is 1");
            }
            else
            {
                for (i = 1; i <= num;i++)
                {
                    factorial = factorial * i;

                    
                }
                textBox2.Text = Convert.ToString(factorial);
                
            }
        }
    }
}
