# This code is compatible with Terraform 4.25.0 and versions that are backwards compatible to 4.25.0.
# For information about validating this Terraform code, see https://developer.hashicorp.com/terraform/tutorials/gcp-get-started/google-cloud-platform-build#format-and-validate-the-configuration

resource "google_compute_instance" "instance-4" {
  boot_disk {
    auto_delete = true
    device_name = "instance-4"

    initialize_params {
      image = "projects/cos-cloud/global/images/cos-stable-105-17412-1-75"
      size  = 10
      type  = "pd-balanced"
    }

    mode = "READ_WRITE"
  }

  can_ip_forward      = false
  deletion_protection = false
  enable_display      = false

  labels = {
    container-vm = "cos-stable-105-17412-1-75"
    ec-src       = "vm_add-tf"
  }

  machine_type = "f1-micro"

  metadata = {
    gce-container-declaration = "spec:\n  containers:\n  - name: instance-4\n    image: us-central1-docker.pkg.dev/juan-camargo/teste/simpleserver_mtst_socrates:latest\n    stdin: true\n    tty: false\n  restartPolicy: Always\n# This container declaration format is not public API and may change without notice. Please\n# use gcloud command-line tool or Google Cloud Console to run Containers on Google Compute Engine."
  }

  name = "instance-4"

  network_interface {
    access_config {
      network_tier = "PREMIUM"
    }

    subnetwork = "projects/juan-camargo/regions/us-central1/subnetworks/default"
  }

  scheduling {
    automatic_restart   = true
    on_host_maintenance = "MIGRATE"
    preemptible         = false
    provisioning_model  = "STANDARD"
  }

  service_account {
    email  = "s403-415@juan-camargo.iam.gserviceaccount.com"
    scopes = ["https://www.googleapis.com/auth/cloud-platform"]
  }

  shielded_instance_config {
    enable_integrity_monitoring = true
    enable_secure_boot          = false
    enable_vtpm                 = true
  }

  tags = ["http-server", "https-server"]
  zone = "us-central1-a"
}
