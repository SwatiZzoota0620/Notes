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
    public partial class Form4 : Form
    {
        public Form4()
        {
            InitializeComponent();
        }

        private void form1ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Form1 f1 = new Form1();
            f1.MdiParent = this;
            f1.Show();
        }

        private void form2ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Form5 f2 = new Form5();
            f2.MdiParent = this;
            f2.Show();

        }


        private void exitToolStripMenuItem_Click(object sender, EventArgs e)
        {
            this.Close();

        }
    }
}
