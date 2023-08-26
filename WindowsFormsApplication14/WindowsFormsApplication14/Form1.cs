using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication14
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

       

        private void button8_Click(object sender, EventArgs e)
        {
            flowLayoutPanel1.FlowDirection = FlowDirection.LeftToRight;
            
         
           
         
        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void button9_Click(object sender, EventArgs e)
        {
            flowLayoutPanel1.FlowDirection = FlowDirection.TopDown;
        }

        private void button10_Click(object sender, EventArgs e)
        {
            flowLayoutPanel1.FlowDirection = FlowDirection.RightToLeft;
        }

        private void button11_Click(object sender, EventArgs e)
        {
            flowLayoutPanel1.FlowDirection = FlowDirection.BottomUp;
        }

        private void button12_Click(object sender, EventArgs e)
        {
            flowLayoutPanel1.AutoScroll = true;
        }

        private void button13_Click(object sender, EventArgs e)
        {
            flowLayoutPanel1.BorderStyle = BorderStyle.FixedSingle;
        }
    }
}
