using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.IO;

namespace WindowsFormsApplication12
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
    

            using (StreamWriter wr = new StreamWriter(@"C:\Users\HP\Documents\Visual Studio 2010\Projects\WindowsFormsApplication12\WindowsFormsApplication12\documents\swati.txt"))
            {
                wr.WriteLine(richTextBox1.Text);
                MessageBox.Show("Successfully updated");
            } 
            

            

        }
    }
}
